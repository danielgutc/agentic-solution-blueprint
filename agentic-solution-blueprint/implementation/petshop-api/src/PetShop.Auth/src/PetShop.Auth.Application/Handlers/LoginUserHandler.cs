namespace PetShop.Auth.Application.Handlers;

using MediatR;
using PetShop.Auth.Application.Commands;
using PetShop.Auth.Application.DTOs;
using PetShop.Users.Domain.Entities;
using PetShop.Users.Infrastructure.Repositories;
using BCrypt.Net;

public class LoginUserHandler : IRequestHandler<LoginUserCommand, Result<AuthResponse>>
{
    private readonly IUserRepository _userRepository;
    private readonly ITokenService _tokenService;

    public LoginUserHandler(IUserRepository userRepository, ITokenService tokenService)
    {
        _userRepository = userRepository;
        _tokenService = tokenService;
    }

    public async Task<Result<AuthResponse>> Handle(LoginUserCommand request, CancellationToken cancellationToken)
    {
        var user = await _userRepository.GetByEmailAsync(request.Email, cancellationToken);
        if (user == null || !BCrypt.Net.BCrypt.Verify(request.Password, user.PasswordHash))
            return Result<AuthResponse>.Failure("Invalid email or password.");

        var tokens = _tokenService.GenerateTokens(user);
        return Result<AuthResponse>.Success(tokens);
    }
}
