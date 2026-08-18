namespace PetShop.Auth.Application.DTOs;

public record AuthResponse(
    string AccessToken,
    string RefreshToken,
    int ExpiresIn
);

public record RegisterRequest(
    string Email,
    string Password,
    string FirstName,
    string LastName
);

public record LoginRequest(
    string Email,
    string Password
);

public record RefreshRequest(
    string RefreshToken
);

public record LogoutRequest(
    string AccessToken
);
