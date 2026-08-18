namespace PetShop.Auth.Api;

using MediatR;
using PetShop.Auth.Application.Handlers;
using PetShop.Auth.Infrastructure;
using FluentValidation;

public static class AuthApiExtensions
{
    public static IServiceCollection AddAuthApi(this IServiceCollection services)
    {
        services.AddMediatR(cfg =>
            cfg.RegisterServicesFromAssembly(typeof(RegisterUserHandler).Assembly));

        services.AddValidatorsFromAssembly(typeof(RegisterUserHandler).Assembly);
        services.AddAuthInfrastructure();

        return services;
    }
}
