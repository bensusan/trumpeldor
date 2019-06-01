using System;
using System.Collections.Generic;
using System.Text;


namespace trumpeldor
{
    public static class PhotosCombiner
    {
        /*
        public static Bitmap MergeTwoImages(Image firstImage, Image secondImage)
    {
        if (firstImage == null)
        {
            throw new ArgumentNullException("firstImage");
        }

        if (secondImage == null)
        {
            throw new ArgumentNullException("secondImage");
        }

        int outputImageWidth = firstImage.Width > secondImage.Width ? firstImage.Width : secondImage.Width;

        int outputImageHeight = firstImage.Height + secondImage.Height + 1;

        Bitmap outputImage = new Bitmap(outputImageWidth, outputImageHeight, System.Drawing.Imaging.PixelFormat.Format32bppArgb);

        using (Graphics graphics = Graphics.FromImage(outputImage))
        {
            graphics.DrawImage(firstImage, new Rectangle(new Point(), firstImage.Size),
                new Rectangle(new Point(), firstImage.Size), GraphicsUnit.Pixel);
            graphics.DrawImage(secondImage, new Rectangle(new Point(0, firstImage.Height + 1), secondImage.Size),
                new Rectangle(new Point(), secondImage.Size), GraphicsUnit.Pixel);
        }

        return outputImage;
    }*/
        //public static Bitmap mergeBitmap(Android.Graphics.Bitmap backBitmap, Android.Graphics.Bitmap frontBitmap)
        //{
        //    Bitmap bitmap = backBitmap.Copy(Android.Graphics.Bitmap.Config.Argb8888, true);
        //    Canvas canvas = new Canvas(bitmap);
        //    Rect baseRect = new Rect(0, 0, backBitmap.Width, backBitmap.Height);
        //    Rect frontRect = new Rect(0, 0, frontBitmap.Width, frontBitmap.Height);
        //    canvas.DrawBitmap(frontBitmap, frontRect, baseRect, null);
        //    return bitmap;
        //}
    }
}
