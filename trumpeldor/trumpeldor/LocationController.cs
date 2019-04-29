﻿using Plugin.Geolocator.Abstractions;
using System;
using System.Collections.Generic;
using System.Text;

namespace trumpeldor
{
    public class LocationController
    {
        private static LocationController instance = null;
        private List<Position> allPositions = null;

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

        public void AddToPositionsHistory(Position p)
        {
            allPositions.Add(p);
        }

        public int GetListCount()
        {
            return allPositions.Count;
        }

        public List<Position> GetStoredPositions()
        {
            return allPositions;
        }

        public double DistanceBetween(double lat1, double lon1, double lat2, double lon2)//distance in meters
        {
            double R = 6371000; // Radius of the earth in meters
            double dLat = deg2rad(lat2 - lat1);  // deg2rad below
            double dLon = deg2rad(lon2 - lon1);
            double a =
              Math.Sin(dLat / 2) * Math.Sin(dLat / 2) +
              Math.Cos(deg2rad(lat1)) * Math.Cos(deg2rad(lat2)) *
              Math.Sin(dLon / 2) * Math.Sin(dLon / 2)
              ;
            double c = 2 * Math.Atan2(Math.Sqrt(a), Math.Sqrt(1 - a));
            double d = R * c;
            return d;
        }

        public double deg2rad(double deg)
        {
            return deg * (Math.PI / 180);
        }
    }
}