namespace PetShop.Users.Application.Handlers;

using MediatR;
using PetShop.Users.Application.DTOs;
using PetShop.Users.Application.Queries;
using PetShop.Users.Domain.Entities;
using PetShop.Users.Infrastructure.Repositories;

public class GetProfileHandler : IRequestHandler<GetProfileQuery, Result<UserProfileResponse>>
{
    private readonly IUserRepository _userRepository;

    public GetProfileHandler(IUserRepository userRepository)
    {
        _userRepository = userRepository;
    }

    public async Task<Result<UserProfileResponse>> Handle(GetProfileQuery request, CancellationToken cancellationToken)
    {
        var user = await _userRepository.GetByIdAsync(request.UserId, cancellationToken);
        if (user == null || user.IsDeleted)
            return Result<UserProfileResponse>.Failure("User not found.");

        return Result<UserProfileResponse>.Success(MapToResponse(user));
    }

    private static UserProfileResponse MapToResponse(User user)
    {
        return new UserProfileResponse(
            user.Id, user.Email, user.FirstName, user.LastName,
            user.Phone, user.Address, user.Role);
    }
}
