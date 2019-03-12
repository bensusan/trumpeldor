using Xamarin.Forms;
using trumpeldor.Droid;
using AVFoundation;
using Foundation;
using System.IO;
using trumpeldor.SheredClasses;

[assembly: Dependency(typeof(AudioRender))]

namespace trumpeldor.Droid
{
    public class AudioRender : IAudioService
    {
        public void PlayAudioFile(string fileName)
        {
            NSError err;
            var player = new AVAudioPlayer(new NSUrl(fileName), "MP3", out err);
            player.FinishedPlaying += delegate
            {
                player = null;
            };
            player.Play();
        }
    }
}