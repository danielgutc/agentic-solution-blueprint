using Serilog;

var logger = Serilog.Log.Logger;
try
{
    logger.Information("Starting PetShop.Api");
    Program.CreateBuilder(args).Build().Run();
}
catch (Exception ex)
{
    logger.Fatal(ex, "PetShop.Api terminated unexpectedly");
}
finally
{
    await Serilog.Log.CloseAndFlushAsync();
}
