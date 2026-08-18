namespace PetShop.Shared.Domain;

public class Result<T>
{
    public bool IsSuccess { get; }
    public T? Value { get; }
    public string? Error { get; }

    private Result(bool isSuccess, T? value, string? error)
    {
        IsSuccess = isSuccess;
        Value = value;
        Error = error;
    }

    public static Result<T> Success(T value) => new(true, value, null);
    public static Result<T> Failure(string error) => new(false, default, error);
    public static Result<T> Failure(IEnumerable<string> errors) => new(false, default, string.Join(", ", errors));
}

public static class Result
{
    public static Result<T> Ok<T>(T value) => Result<T>.Success(value);
    public static Result Failure(string error) => Result<string>.Failure(error);
}
