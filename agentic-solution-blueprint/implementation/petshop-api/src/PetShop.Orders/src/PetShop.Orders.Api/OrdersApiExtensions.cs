namespace PetShop.Orders.Api;

using MediatR;
using PetShop.Orders.Application.Handlers;
using PetShop.Orders.Infrastructure;
using FluentValidation;

public static class OrdersApiExtensions
{
    public static IServiceCollection AddOrdersApi(this IServiceCollection services)
    {
        services.AddMediatR(cfg =>
            cfg.RegisterServicesFromAssembly(typeof(PlaceOrderHandler).Assembly));

        services.AddValidatorsFromAssembly(typeof(PlaceOrderHandler).Assembly);
        services.AddOrdersInfrastructure();

        return services;
    }
}
