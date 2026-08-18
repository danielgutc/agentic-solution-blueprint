namespace PetShop.Catalog.Api;

using Microsoft.Extensions.DependencyInjection;
using PetShop.Catalog.Application.Handlers;
using PetShop.Catalog.Infrastructure;
using FluentValidation;
using MediatR;

public static class CatalogApiExtensions
{
    public static IServiceCollection AddCatalogApi(this IServiceCollection services)
    {
        services.AddMediatR(cfg =>
            cfg.RegisterServicesFromAssembly(typeof(CreateProductHandler).Assembly));

        services.AddValidatorsFromAssembly(typeof(CreateProductHandler).Assembly);

        services.AddCatalogInfrastructure();

        return services;
    }
}
