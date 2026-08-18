namespace PetShop.Catalog.Infrastructure;

using Microsoft.Extensions.DependencyInjection;
using PetShop.Catalog.Infrastructure.Repositories;
using PetShop.Catalog.Infrastructure.Caching;

public static class CatalogServiceCollectionExtensions
{
    public static IServiceCollection AddCatalogInfrastructure(this IServiceCollection services)
    {
        services.AddScoped<IProductRepository, ProductRepository>();
        services.AddScoped<ICategoryRepository, CategoryRepository>();
        services.AddScoped<IInventoryRepository, InventoryRepository>();
        services.AddScoped<IProductCacheService, ProductCacheService>();

        return services;
    }
}
