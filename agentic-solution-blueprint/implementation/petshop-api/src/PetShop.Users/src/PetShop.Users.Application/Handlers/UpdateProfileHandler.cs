namespace PetShop.Users.Application.Handlers;

using MediatR;
using PetShop.Users.Application.Commands;
using PetShop.Users.Application.DTOs;
using PetShop.Users.Domain.Entities;
using PetShop.Users.Infrastructure.Repositories;

public class UpdateProfileHandler : IRequestHandler<UpdateProfileCommand, Result<UserProfileResponse>>
{
    private readonly IUserRepository _userRepository;

    public UpdateProfileHandler(IUserRepository userRepository)
    {
        _userRepository = userRepository;
    }

    public async Task<Result<UserProfileResponse>> Handle(UpdateProfileCommand request, CancellationToken cancellationToken)
    {
        var user = await _userRepository.GetByIdAsync(request.UserId, cancellationToken);
        if (user == null || user.IsDeleted)
            return Result<UserProfileResponse>.Failure("User not found.");

        user.UpdateProfile(request.FirstName, request.LastName, request.Phone, request.Address);
        await _userRepository.UpdateAsync(user, cancellationToken);

        return Result<UserProfileResponse>.Success(MapToResponse(user));
    }

    private static UserProfileResponse MapToResponse(User user)
    {
        return new UserProfileResponse(
            user.Id, user.Email, user.FirstName, user.LastName,
            user.Phone, user.Address, user.Role);
    }
}
