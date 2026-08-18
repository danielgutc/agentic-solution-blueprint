namespace PetShop.Users.Infrastructure;

using Microsoft.Extensions.DependencyInjection;
using PetShop.Users.Infrastructure.Repositories;

public static class UsersServiceCollectionExtensions
{
    public static IServiceCollection AddUsersInfrastructure(this IServiceCollection services)
    {
        services.AddScoped<IUserRepository, UserRepository>();
        return services;
    }
}
