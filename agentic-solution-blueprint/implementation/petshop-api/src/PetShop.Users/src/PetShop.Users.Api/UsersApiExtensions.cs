namespace PetShop.Users.Api;

using MediatR;
using PetShop.Users.Application.Handlers;
using PetShop.Users.Infrastructure;
using FluentValidation;

public static class UsersApiExtensions
{
    public static IServiceCollection AddUsersApi(this IServiceCollection services)
    {
        services.AddMediatR(cfg =>
            cfg.RegisterServicesFromAssembly(typeof(UpdateProfileHandler).Assembly));

        services.AddValidatorsFromAssembly(typeof(UpdateProfileHandler).Assembly);
        services.AddUsersInfrastructure();

        return services;
    }
}
