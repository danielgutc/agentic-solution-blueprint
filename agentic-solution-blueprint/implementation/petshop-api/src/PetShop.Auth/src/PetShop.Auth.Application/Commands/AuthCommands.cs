namespace PetShop.Auth.Application.Commands;

using MediatR;
using PetShop.Auth.Application.DTOs;

public record RegisterUserCommand(
    string Email,
    string Password,
    string FirstName,
    string LastName
) : IRequest<Result<AuthResponse>>;

public record LoginUserCommand(
    string Email,
    string Password
) : IRequest<Result<AuthResponse>>;

public record RefreshTokenCommand(
    string RefreshToken
) : IRequest<Result<AuthResponse>>;

public record LogoutUserCommand(
    Guid UserId,
    string RefreshToken
) : IRequest<Result>;
