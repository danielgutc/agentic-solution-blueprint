namespace PetShop.Catalog.Infrastructure.Caching;

using PetShop.Catalog.Application.DTOs;
using PetShop.Shared.Domain;

public interface IProductCacheService
{
    Task<Paging<ProductResponse>?> GetProductsCacheAsync(string key, CancellationToken cancellationToken = default);
    Task SetProductsCacheAsync(string key, Paging<ProductResponse> value, TimeSpan ttl, CancellationToken cancellationToken = default);
    Task ClearProductsCacheAsync(CancellationToken cancellationToken = default);
    Task<ProductResponse?> GetProductCacheAsync(string key, CancellationToken cancellationToken = default);
    Task SetProductCacheAsync(string key, ProductResponse value, TimeSpan ttl, CancellationToken cancellationToken = default);
}
