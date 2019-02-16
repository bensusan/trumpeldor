using System.Threading;
using System.Threading.Tasks;

namespace trumpeldor.Configuration
{
    public interface IConfigurationManager
    {
        Task<Configuration> GetAsync(CancellationToken cancellationToken);
    }
}
