class Program
{
    static Task bar()
    {
        return Task.Delay(TimeSpan.FromSeconds(5)).ContinueWith(t =>
        {
            Console.WriteLine("Bar");
        });
    }

    static async Task foo()
    {
        Console.WriteLine("Before");

        await bar();

        Console.WriteLine("After");
    }


    static void Main(string[] args)
    {
        foo().Wait();
    }
}
