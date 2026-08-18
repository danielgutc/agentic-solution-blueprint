namespace PetShop.Users.Application.DTOs;

public record UserProfileResponse(
    Guid Id,
    string Email,
    string FirstName,
    string LastName,
    string? Phone,
    string? Address,
    UserRole Role
);

public record UpdateProfileRequest(
    string? FirstName,
    string? LastName,
    string? Phone,
    string? Address
);
