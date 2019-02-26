using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace trumpeldor.SheredClasses
{
    public class Trip
    {
        public int id { get; set; }
        public User user { get; set; }
        public string groupName { get; set; }
        public List<int> playersAges { get; set; }
        public int score { get; set; }
        public Track track { get; set; }
        public List<Attraction> attractionsDone { get; set; }
        public List<FeedbackInstance> feedbacks { get; set; }

        internal Attraction GetCurrentAttraction()
        {
            return attractionsDone[attractionsDone.Count - 1];
        }

        private Attraction FindClosestAttraction(double userLocationX, double userLocationY, List<Attraction> attractions)
        {
            double minDistacnce = Views.MapPage.DistanceBetween(userLocationX, userLocationY, attractions[0].x, attractions[0].y);
            Attraction closestAttraction = attractions[0];
            for(int i=1; i<attractions.Count; i++)
            {
                double distance = Views.MapPage.DistanceBetween(userLocationX, userLocationY, attractions[i].x, attractions[i].y);
                if (distance < minDistacnce)
                {
                    minDistacnce = distance;
                    closestAttraction = attractions[i];
                }
            }
            return closestAttraction;
        }

        internal bool DoneMyAttraction(double userLocationX, double userLocationY)
        {
            List<Attraction> allAttractions = track.GetAllPoints();
            List<Attraction> relevantAttractions = difference(allAttractions, attractionsDone);
            if (relevantAttractions.Count == 0)
                return true;
            Attraction toAdd = FindClosestAttraction(userLocationX, userLocationY, relevantAttractions);
            attractionsDone.Add(toAdd);
            return false;

        }

        private List<Attraction> difference(List<Attraction> a1, List<Attraction> a2)
        {
            List<Attraction> ans = new List<Attraction>();
            bool isInA2;
            for(int i=0; i<a1.Count; i++)
            {
                isInA2 = false;
                for(int j = 0; j < a2.Count; j++)
                {
                    if (a1[i].id == a2[j].id)
                    {
                        isInA2 = true;
                    }
                }
                if (!isInA2)
                    ans.Add(a1[i]);
            }
            return ans;
        }
    }
}
