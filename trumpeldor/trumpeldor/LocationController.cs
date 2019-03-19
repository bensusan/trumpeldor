using Plugin.Geolocator.Abstractions;
using System;
using System.Collections.Generic;
using System.Text;

namespace trumpeldor
{
    class LocationController
    {
        private static LocationController instance = null;
        private static List<Position> allPositions = null;

        private LocationController()
        {
            allPositions = new List<Position>();
        }

        public static LocationController GetInstance()
        {
            if (instance == null)
            {
                instance = new LocationController();
            }
            return instance;
        }
         
    }
}
