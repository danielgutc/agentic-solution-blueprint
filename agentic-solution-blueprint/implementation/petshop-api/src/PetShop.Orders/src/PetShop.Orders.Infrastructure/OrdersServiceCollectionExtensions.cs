namespace PetShop.Orders.Infrastructure;

using Microsoft.Extensions.DependencyInjection;
using PetShop.Orders.Infrastructure.Repositories;
using PetShop.Orders.Infrastructure.Messaging;

public static class OrdersServiceCollectionExtensions
{
    public static IServiceCollection AddOrdersInfrastructure(this IServiceCollection services)
    {
        services.AddScoped<IOrderRepository, OrderRepository>();
        services.AddScoped<IOrderEventPublisher, OrderEventPublisher>();
        return services;
    }
}
