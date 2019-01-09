using System;
using System.Collections.Generic;
using System.Text;

namespace trumpeldor.SheredClasses
{
    public class Attraction
    {
        public int id { get; set; }
        public string name { get; set; }
        public float x { get; set; }
        public float y { get; set; }
        public String description { get; set; }
        public List<string> picturesURLS { get; set; }
        public List<string> videosURLS { get; set; }
        public List<Hint> hints { get; set; }
        public AmericanQuestion americanQuestion { get; set; }

        internal string GetMainPictureUrl()
        {
            return picturesURLS != null && picturesURLS.Count > 0 ? picturesURLS[0] : "";    //TODO: for now return first image.
        }
    }
}
