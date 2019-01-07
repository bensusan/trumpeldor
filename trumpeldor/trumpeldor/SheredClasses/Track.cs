using System;
using System.Collections.Generic;
using System.Text;

namespace trumpeldor.SheredClasses
{
    public class Track
    {
        internal int id { get; set; }
        internal Track subTrack { get; set; }
        internal List<Attraction> pointsNumber { get; set; }
        internal int length { get; set; }

        public Track()
        {
        }
    }
}
