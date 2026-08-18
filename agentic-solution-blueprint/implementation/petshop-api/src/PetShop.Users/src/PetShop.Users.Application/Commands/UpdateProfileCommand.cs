namespace PetShop.Users.Application.Commands;

using MediatR;
using PetShop.Users.Application.DTOs;

public record UpdateProfileCommand(
    Guid UserId,
    string? FirstName,
    string? LastName,
    string? Phone,
    string? Address
) : IRequest<Result<UserProfileResponse>>;
