namespace PetShop.Users.Application.Queries;

using MediatR;
using PetShop.Users.Application.DTOs;

public record GetProfileQuery(Guid UserId) : IRequest<Result<UserProfileResponse>>;
