using System;
using System.Collections.Generic;
using System.IO;
using System.Net.Http;
using System.Threading;
using System.Threading.Tasks;
using Google.Apis.Auth.OAuth2;
using Google.Apis.Auth.OAuth2.Responses;
using Google.Apis.Services;
using Google.Apis.YouTube.v3;
using Newtonsoft.Json;

namespace OpenTelemetryYoutube;

internal class YouTubeServiceHelper
{
    private YouTubeServiceHelper()
    {
        this.ClientId = Environment.GetEnvironmentVariable("YOUTUBE_API_CLIENT_ID");
        this.ClientSecret = Environment.GetEnvironmentVariable("YOUTUBE_API_CLIENT_SECRET");
        this.AccessToken = Environment.GetEnvironmentVariable("YOUTUBE_API_ACCESS_TOKEN");
        this.RefreshToken = Environment.GetEnvironmentVariable("YOUTUBE_API_REFRESH_TOKEN");
    }

    public static YouTubeServiceHelper Instance { get; } = new YouTubeServiceHelper();

    public string ClientId { get; }
    public string ClientSecret { get; }
    public string AccessToken { get; }
    public string RefreshToken { get; }

    public TokenResponse GetTokenResponse()
    {
        var request = new HttpRequestMessage(HttpMethod.Post, "https://accounts.google.com/o/oauth2/token")
        {
            Content = new FormUrlEncodedContent(new Dictionary<string, string>
            {
                { "client_id", this.ClientId },
                { "client_secret", this.ClientSecret },
                { "refresh_token", this.RefreshToken },
                { "grant_type", "refresh_token" },
            }),
        };

        using var client = new HttpClient();
        var response = client.Send(request);
        using var reader = new StreamReader(response.Content.ReadAsStream());
        var json = reader.ReadToEnd();

        var tokenErrorResponse = JsonConvert.DeserializeObject<TokenErrorResponse>(json);
        if (!string.IsNullOrEmpty(tokenErrorResponse.Error))
        {
            throw new Exception($"Received token error response: {json}");
        }

        var tokenResponse = JsonConvert.DeserializeObject<TokenResponse>(json);
        if (string.IsNullOrEmpty(tokenResponse.AccessToken))
        {
            throw new Exception($"Received invalid token response: {json}");
        }

        tokenResponse.IssuedUtc = DateTime.UtcNow;
        return tokenResponse;
    }

    public async Task<YouTubeService> GetYouTubeService()
    {
        var cts = new CancellationTokenSource(10000);
        try
        {
            var credential = await GoogleWebAuthorizationBroker.AuthorizeAsync(
                new ClientSecrets
                {
                    ClientId = this.ClientId,
                    ClientSecret = this.ClientSecret,
                },
                new[] { YouTubeService.Scope.Youtube },
                "user",
                cts.Token,
                new YouTubeToolDataStore()
            );

            return new YouTubeService(new BaseClientService.Initializer
            {
                HttpClientInitializer = credential,
                ApplicationName = typeof(Program).ToString(),
            });
        }
        catch (OperationCanceledException e)
        {
            throw new TimeoutException("Timed out authorizing with YouTube API. Token has likely expired.", e);
        }
        finally
        {
            cts.Dispose();
        }
    }
}
