namespace PetShop.Auth.Infrastructure;

using Microsoft.Extensions.DependencyInjection;
using PetShop.Auth.Application.Services;
using PetShop.Auth.Infrastructure.Services;

public static class AuthServiceCollectionExtensions
{
    public static IServiceCollection AddAuthInfrastructure(this IServiceCollection services)
    {
        services.AddScoped<ITokenService, JwtTokenService>();
        return services;
    }
}
