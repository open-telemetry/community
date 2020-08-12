using System;
using System.IO;
using System.Linq;
using System.Threading;
using System.Threading.Tasks;
using System.Xml;
using Google.Apis.Auth.OAuth2;
using Google.Apis.Services;
using Google.Apis.Util.Store;
using Google.Apis.YouTube.v3;
using Google.Apis.YouTube.v3.Data;

namespace OpenTelemetryYoutube
{
    class Program
    {
        [STAThread]
        static void Main(string[] args)
        {
            try
            {
                Console.WriteLine("Path to secret.json");
                string path = Console.ReadLine();

                new Program().Run(path).Wait();
            }
            catch (AggregateException ex)
            {
                foreach (var e in ex.InnerExceptions)
                {
                    Console.WriteLine("Error: " + e.Message);
                }
            }
        }

        private async Task Run(string path)
        {
            UserCredential credential;
            using (var stream = new FileStream(path, FileMode.Open, FileAccess.Read))
            {
                credential = await GoogleWebAuthorizationBroker.AuthorizeAsync(
                    GoogleClientSecrets.Load(stream).Secrets,
                    new[] { YouTubeService.Scope.Youtube },
                    "user",
                    CancellationToken.None,
                    new FileDataStore(this.GetType().ToString())
                );
            }

            var youtubeService = new YouTubeService(new BaseClientService.Initializer
            {
                HttpClientInitializer = credential,
                ApplicationName = this.GetType().ToString(),
            });

            var channelsListRequest = youtubeService.Channels.List("snippet,contentDetails,statistics");
            channelsListRequest.Mine = true;

            // Retrieve the contentDetails part of the channel resource for the authenticated user's channel.
            var channelsListResponse = await channelsListRequest.ExecuteAsync();

            foreach (var channel in channelsListResponse.Items)
            {
                await ProcessChannel(youtubeService, channel);
            }
        }

        private static async Task ProcessChannel(YouTubeService youtubeService, Channel channel)
        {
            // From the API response, extract the playlist ID that identifies the list
            // of videos uploaded to the authenticated user's channel.
            var uploadsListId = channel.ContentDetails.RelatedPlaylists.Uploads;

            Console.WriteLine("Videos in list {0}", uploadsListId);

            var nextPageToken = "";
            while (nextPageToken != null)
            {
                var playlistItemsListRequest = youtubeService.PlaylistItems.List("snippet,contentDetails,status");
                playlistItemsListRequest.PlaylistId = uploadsListId;
                playlistItemsListRequest.MaxResults = 50;
                playlistItemsListRequest.PageToken = nextPageToken;

                // Retrieve the list of videos uploaded to the authenticated user's channel.
                var playlistItemsListResponse = await playlistItemsListRequest.ExecuteAsync();

                foreach (var playlistItem in playlistItemsListResponse.Items.Where(q => q.Status.PrivacyStatus == "private"))
                {
                    // Print information about each video.
                    Console.WriteLine("{0} ({1})", playlistItem.Snippet.Title, playlistItem.Snippet.ResourceId.VideoId);

                    var videoItemRequest = youtubeService.Videos.List("snippet,contentDetails,statistics");
                    videoItemRequest.Id = playlistItem.Snippet.ResourceId.VideoId;

                    var videoItemResponse = await videoItemRequest.ExecuteAsync();

                    foreach (var videoItem in videoItemResponse.Items)
                    {
                        await ProcessVideo(youtubeService, videoItem);
                    }
                }

                nextPageToken = playlistItemsListResponse.NextPageToken;
            }
        }

        private static async Task ProcessVideo(YouTubeService youtubeService, Video videoItem)
        {
            var time = XmlConvert.ToTimeSpan(videoItem.ContentDetails.Duration);

            // video that doesn't start with 202x and has totalMinutes > 30, we will process
            if (!videoItem.Snippet.Title.StartsWith("202") && time.TotalMinutes > 30)
            {
                Video video = new Video
                {
                    Id = videoItem.Id,
                    Snippet = new VideoSnippet
                    {
                        CategoryId = "22",
                        Title = $"{videoItem.Snippet.PublishedAt.Split('T')[0]} meeting"
                    },
                    Status = new VideoStatus
                    {
                        PrivacyStatus = "public"
                    }
                };

                var videoUpdateRequest = youtubeService.Videos.Update(video, "snippet,status");
                await videoUpdateRequest.ExecuteAsync();
            }
        }
    }
}
