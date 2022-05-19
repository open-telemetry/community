using System;
using System.Threading;
using System.Threading.Tasks;
using Google.Apis.Auth.OAuth2;
using Google.Apis.Auth.OAuth2.Responses;
using Google.Apis.Services;
using Google.Apis.YouTube.v3;

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
        return new TokenResponse
        {
            AccessToken = this.AccessToken,
            ExpiresInSeconds = 3599,
            RefreshToken = this.RefreshToken,
            Scope = "https://www.googleapis.com/auth/youtube",
            TokenType = "Bearer",
            IssuedUtc = System.DateTime.UtcNow,
        };
    }

    public async Task<YouTubeService> GetYouTubeService()
    {
        var credential = await GoogleWebAuthorizationBroker.AuthorizeAsync(
            new ClientSecrets
            {
                ClientId = this.ClientId,
                ClientSecret = this.ClientSecret,
            },
            new[] { YouTubeService.Scope.Youtube },
            "user",
            CancellationToken.None,
            new YouTubeToolDataStore()
        );

        return new YouTubeService(new BaseClientService.Initializer
        {
            HttpClientInitializer = credential,
            ApplicationName = typeof(Program).ToString(),
        });
    }
}
