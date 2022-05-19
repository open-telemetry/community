using System;
using System.Threading.Tasks;
using Google.Apis.Util.Store;

namespace OpenTelemetryYoutube;

internal class YouTubeToolDataStore : IDataStore
{
    public Task ClearAsync()
    {
        return Task.FromResult(0);
    }

    public Task DeleteAsync<T>(string key)
    {
        return Task.FromResult(0);
    }

    public Task<T> GetAsync<T>(string key)
    {
        if (string.IsNullOrEmpty(key))
        {
            throw new ArgumentException("Key MUST have a value");
        }

        TaskCompletionSource<T> tcs = new TaskCompletionSource<T>();
        if (YouTubeServiceHelper.Instance.GetTokenResponse() is T tokenResponse)
        {
            tcs.SetResult(tokenResponse);
        }
        else
        {
            throw new ArgumentException($"Type '{typeof(T)}' unsupported");
        }

        return tcs.Task;
    }

    public Task StoreAsync<T>(string key, T value)
    {
        return Task.FromResult(0);
    }
}
