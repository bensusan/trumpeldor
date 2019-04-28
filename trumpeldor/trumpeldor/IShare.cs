using System;
using System.Collections.Generic;
using System.Text;
using System.Threading.Tasks;
using Xamarin.Forms;

namespace trumpeldor
{
    public interface IShare
    {
        Task ShareOnSocialMedia(string imageName);
        void ShareOnSocialMedia(string message, ImageSource image);
    }
}
