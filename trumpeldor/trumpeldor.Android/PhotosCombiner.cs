using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using Android.App;
using Android.Content;
using Android.Graphics;
using Android.OS;
using Android.Runtime;
using Android.Views;
using Android.Widget;

namespace trumpeldor.Droid
{
    public static class PhotosCombiner
    {
        public static Android.Graphics.Bitmap mergeBitmap(Android.Graphics.Bitmap backBitmap, Android.Graphics.Bitmap frontBitmap)
        {
            Android.Graphics.Bitmap bitmap = backBitmap.Copy(Android.Graphics.Bitmap.Config.Argb8888, true);
            Canvas canvas = new Canvas(bitmap);
            Rect baseRect = new Rect(0, 0, backBitmap.Width, backBitmap.Height);
            Rect frontRect = new Rect(0, 0, frontBitmap.Width, frontBitmap.Height);
            canvas.DrawBitmap(frontBitmap, frontRect, baseRect, null);
            return bitmap;
        }
    }
}