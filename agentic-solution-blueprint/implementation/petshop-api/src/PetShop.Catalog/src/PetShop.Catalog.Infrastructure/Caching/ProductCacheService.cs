namespace PetShop.Catalog.Infrastructure.Caching;

using Microsoft.Extensions.Caching.Distributed;
using PetShop.Catalog.Application.DTOs;
using PetShop.Shared.Domain;
using System.Text.Json;

public class ProductCacheService : IProductCacheService
{
    private readonly IDistributedCache _cache;
    private readonly JsonSerializerOptions _jsonOptions;

    public ProductCacheService(IDistributedCache cache)
    {
        _cache = cache;
        _jsonOptions = new JsonSerializerOptions { PropertyNameCaseInsensitive = true };
    }

    public async Task<Paging<ProductResponse>?> GetProductsCacheAsync(string key, CancellationToken cancellationToken = default)
    {
        var value = await _cache.GetStringAsync($"products:{key}", cancellationToken);
        if (value == null) return null;

        return JsonSerializer.Deserialize<Paging<ProductResponse>>(value, _jsonOptions);
    }

    public async Task SetProductsCacheAsync(string key, Paging<ProductResponse> value, TimeSpan ttl, CancellationToken cancellationToken = default)
    {
        var json = JsonSerializer.Serialize(value, _jsonOptions);
        await _cache.SetStringAsync($"products:{key}", json, new DistributedCacheEntryOptions { AbsoluteExpirationRelativeToNow = ttl }, cancellationToken);
    }

    public async Task ClearProductsCacheAsync(CancellationToken cancellationToken = default)
    {
        // In production, use cache keys with versioning or namespace prefix
        // For now, this is a placeholder for cache invalidation strategy
    }

    public async Task<ProductResponse?> GetProductCacheAsync(string key, CancellationToken cancellationToken = default)
    {
        var value = await _cache.GetStringAsync($"product:{key}", cancellationToken);
        if (value == null) return null;

        return JsonSerializer.Deserialize<ProductResponse>(value, _jsonOptions);
    }

    public async Task SetProductCacheAsync(string key, ProductResponse value, TimeSpan ttl, CancellationToken cancellationToken = default)
    {
        var json = JsonSerializer.Serialize(value, _jsonOptions);
        await _cache.SetStringAsync($"product:{key}", json, new DistributedCacheEntryOptions { AbsoluteExpirationRelativeToNow = ttl }, cancellationToken);
    }
}
