namespace PetShop.Auth.Application.Handlers;

using MediatR;
using PetShop.Auth.Application.Commands;
using PetShop.Auth.Application.DTOs;
using PetShop.Users.Domain.Entities;
using PetShop.Users.Infrastructure.Repositories;
using BCrypt.Net;

public class RegisterUserHandler : IRequestHandler<RegisterUserCommand, Result<AuthResponse>>
{
    private readonly IUserRepository _userRepository;
    private readonly ITokenService _tokenService;

    public RegisterUserHandler(IUserRepository userRepository, ITokenService tokenService)
    {
        _userRepository = userRepository;
        _tokenService = tokenService;
    }

    public async Task<Result<AuthResponse>> Handle(RegisterUserCommand request, CancellationToken cancellationToken)
    {
        if (await _userRepository.EmailExistsAsync(request.Email, cancellationToken))
            return Result<AuthResponse>.Failure("Email already registered.");

        var passwordHash = BCrypt.Net.BCrypt.HashPassword(request.Password, 12);
        var user = new User(
            Guid.NewGuid(),
            request.Email.Trim().ToLower(),
            passwordHash,
            request.FirstName.Trim(),
            request.LastName.Trim(),
            UserRole.Customer);

        await _userRepository.CreateAsync(user, cancellationToken);

        var tokens = _tokenService.GenerateTokens(user);
        return Result<AuthResponse>.Success(tokens);
    }
}
