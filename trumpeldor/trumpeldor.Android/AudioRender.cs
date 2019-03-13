using Android.Media;
using Xamarin.Forms;
using trumpeldor.Droid;
using trumpeldor.SheredClasses;

[assembly: Dependency(typeof(AudioRender))]
namespace trumpeldor.Droid
{
    public class AudioRender : IAudioService
    {
        public void PlayAudioFile(string fileName)
        {
            var player = new MediaPlayer();
            var file = global::Android.App.Application.Context.Assets.OpenFd(fileName);
            player.SetDataSource(file.FileDescriptor, file.StartOffset, file.Length);
            player.Prepared += (s, e) => { player.Start(); };
            player.Prepare();
        }
    }
}