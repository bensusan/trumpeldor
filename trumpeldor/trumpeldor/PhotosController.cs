using System;
using System.Collections.Generic;
using System.Text;
using Xamarin.Forms;

namespace trumpeldor
{
    public class PhotosController
    {
        private static PhotosController instance = null;
        private List<string> photosSources = null;

        private PhotosController()
        {
            photosSources = new List<string>();
        }

        public static PhotosController GetInstance()
        {
            if (instance == null)
            {
                instance = new PhotosController();
            }
            return instance;
        }

        public void AddToPhotosSourcesList(string src)
        {
            photosSources.Add(src);
        }

        public List<string> GetPhotosSourcesList()
        {
            return photosSources;
        }
    }
}
