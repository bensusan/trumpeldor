using System;
using System.Collections.Generic;
using System.Text;

namespace trumpeldor.SheredClasses
{
    public class Track
    {
        public int id { get; set; }
        public Track subTrack { get; set; }
        public List<Attraction> points { get; set; }
        public int length { get; set; }

        internal List<Attraction> GetAllPoints()
        {
            List<Attraction> myPoints = new List<Attraction>();
            myPoints.AddRange(points);
            if (subTrack == null)
                return myPoints;
            myPoints.AddRange(subTrack.GetAllPoints());
            return myPoints;
        }
    }
}
