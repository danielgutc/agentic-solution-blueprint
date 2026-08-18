namespace PetShop.Auth.Application.Handlers;

using MediatR;
using PetShop.Auth.Application.Commands;
using PetShop.Auth.Application.DTOs;
using PetShop.Auth.Domain.Entities;

public interface ITokenService
{
    AuthResponse GenerateTokens(User user);
    bool ValidateToken(string token);
    void RevokeToken(string refreshToken);
    bool IsTokenRevoked(string refreshToken);
}
