using System;
using System.Collections.Generic;
using System.Text;

namespace trumpeldor.SheredClasses
{
    public class TrackPoint
    {
        private int id;
        private string name="some name";
        private double Latitude;
        private double Longitude;

        public TrackPoint(double Latitude,double Longitude)
        {
            this.Latitude = Latitude;
            this.Longitude = Longitude;
        }
        public double GetLatitude()
        {
            return this.Latitude;
        }
        public double GetLongitude()
        {
            return this.Longitude;
        }
        public int GetID()
        {
            return this.id;
        }

        public string GetName()
        {
            return this.name;
        }
    }
}
