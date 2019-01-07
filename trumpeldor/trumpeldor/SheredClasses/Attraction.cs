using System;
using System.Collections.Generic;
using System.Text;

namespace trumpeldor.SheredClasses
{
    public class Attraction
    {
        internal int id { get; set; }
        internal string name { get; set; }
        internal float x { get; set; }
        internal float y { get; set; }
        internal String description { get; set; }
        internal List<string> picturesURLS { get; set; }
        internal List<string> videosURLS { get; set; }

        public Attraction()
        {
        }

        internal string GetMainPictureUrl()
        {
            return picturesURLS != null && picturesURLS.Count > 0 ? picturesURLS[0] : "";    //TODO: for now return first image.
        }
    }
}
