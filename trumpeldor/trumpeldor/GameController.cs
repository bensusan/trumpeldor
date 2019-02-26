using System;
using System.Collections.Generic;
using System.Text;
using trumpeldor.SheredClasses;
using Plugin.Geolocator;
using Xamarin.Forms.Maps;
using System.Threading.Tasks;
using System.IO;
using Xamarin.Forms;
namespace trumpeldor
{
    public class GameController
    {
        private static GameController instance = null;
        //TODO MAKE TRIP INSTEAD OF SCORE, GROUPNAME, USER, TRACK
        public Trip currentTrip = null;
        public User currentUser = null; //Also will show in Trip object but necessary also.
        //public enum PathLength { shortPath = 1, mediumPath = 2, longPath = 3 }
        private ServerConection conn;
        //private String groupName;
        //public int score;
        private Dictionary<Attraction,Boolean> destinations;
        public bool isFinishTrip;

        //private PathLength currentPathLength;
        //public Attraction currentAttractionDestination = null;
        const int LOGIN_RECENETLY_DIFFERENCE_HOURS = 36; //TODO - Very specific for now
        //float latitude = 0;
        //float longtitude = 0;
        public Track extendTrack = null;

        public static GameController getInstance()
        {
            if (instance == null)
            {
                ServerConection serverConnection = ServerConection.getInstance();
                instance = new GameController(serverConnection);
            }
            return instance;
        }

        internal bool IsNewUser()
        {
            return currentUser.lastSeen == null;
        }

        internal int GetScore()
        {
            return currentTrip.score;
        }

        private int GetNextPathLength(int pl)
        {
            return pl + 1;
        }

        public bool IsUserConnectedRecently()
        {
            return !this.IsNewUser() && 
                (DateTime.Now - (DateTime)currentUser.lastSeen).TotalHours <= LOGIN_RECENETLY_DIFFERENCE_HOURS;
        }

        internal async Task<Attraction> GetTempAttraction()
        {
            return await conn.GetAttractionForDebug();
        }

        internal async Task<RelevantInformation> LoadRelevantInformationFromLastTrip()
        {
            return await conn.LoadRelevantInformationFromLastTrip(currentUser);
        }

        internal async Task FinishAttraction()
        {
            SheredClasses.Point userLocation = await GetUserLocation();
            isFinishTrip = this.currentTrip.DoneMyAttraction(userLocation.x, userLocation.y);
        }

        internal async Task ContinuePreviousTrip()
        {
            this.currentTrip = await conn.GetPreviousTrip(currentUser);
        }

        private GameController(ServerConection serverConnection)
        {
            this.conn = serverConnection;
            destinations = new Dictionary<Attraction, bool>();
        }

        public async Task CreateTrip(string groupName, List<int> playersAges, int trackLength)
        {
            SheredClasses.Point userLocation = await GetUserLocation();
            currentTrip = await conn.CreateTripAsync(currentUser, groupName, playersAges, trackLength, userLocation.x, userLocation.y);
        }

        private async Task <SheredClasses.Point> GetUserLocation()
        {
            var locator = CrossGeolocator.Current;
            Plugin.Geolocator.Abstractions.Position position = await locator.GetPositionAsync(TimeSpan.FromSeconds(10));
            return new SheredClasses.Point(position.Latitude, position.Longitude);
            //return new SheredClasses.Point(31.262960, 34.797152); 
        }

        //private float GetUserY()
        //{
        //    if(latitude==0 && longtitude==0)
        //    {
        //        GetLocation();
        //        return longtitude;
        //    }
        //    return longtitude;
        //}

        //private float GetUserX()
        //{
        //    if(latitude==0 && longtitude==0)
        //    {
        //        GetLocation();
        //        return longtitude;
        //    }
        //    return longtitude;
        //}

        //private async void GetLocation()
        //{
        //    var locator = CrossGeolocator.Current;
        //    var position = await locator.GetPositionAsync(TimeSpan.FromSeconds(10));
        //    latitude = (float)position.Latitude;
        //    longtitude = (float)position.Longitude;
        //}
        
        public Clue GetFisrtHint()
        {
            //TODO
            return new TextClue();
        }

        public Clue GetHint()
        {
            //TODO
            return new TextClue();
        }

        //get y.png for example return http://IP:PORT/media/y.png
        public string GetImageURLFromName(string pictureName)
        {
            return "http://" + ServerConection.IP + ":" + ServerConection.PORT + "/media/" + pictureName;
        }

        public String GetGeneralInformation()
        {
            return "some general information";
        }

        public async Task<bool> CanContinueToLongerTrack()
        {
            trumpeldor.SheredClasses.Point userLocation = await GetUserLocation();
            this.extendTrack = await conn.GetExtendedTrack(this.currentTrip.track, userLocation);
            return this.extendTrack != null;
        }

        public void ContinueToLongerTrack()
        {
           
        }

        public List<Attraction> GetVisitedAttractions()
        {
            List<Attraction> visitedAttractions = new List<Attraction>();
            foreach (Attraction Attraction in destinations.Keys)
            {
                if (destinations[Attraction])
                {
                    visitedAttractions.Add(Attraction);
                }
            }
            return visitedAttractions;
        }



        /*private double GetDistanceFromLatLonInKm(double lat1, double lon1, double lat2, double lon2)
        {
            double R = 6371; // Radius of the earth in km
            double dLat = Deg2rad(lat2 - lat1);  // deg2rad below
            double dLon = Deg2rad(lon2 - lon1);
            double a =
              Math.Sin(dLat / 2) * Math.Sin(dLat / 2) +
              Math.Cos(Deg2rad(lat1)) * Math.Cos(Deg2rad(lat2)) *
              Math.Sin(dLon / 2) * Math.Sin(dLon / 2);
            double c = 2 * Math.Atan2(Math.Sqrt(a), Math.Sqrt(1 - a));
            double d = R * c; // Distance in km
            return d;
        }
        private double Deg2rad(double deg)
        {
            return deg * (Math.PI / 180);
        }
        private void SelectNextAttractionHelper(double latitude, double longitude)
        {
            double ShortestDistance = double.MaxValue;
            Attraction closestAttraction = null;


            foreach (Attraction tp in destinations.Keys)
            {
                if(!destinations[tp])//we dont visit at tp
                {
                    
                    double distance=GetDistanceFromLatLonInKm(position.Latitude, position.Longitude, tp.GetLatitude(), tp.GetLongitude());
                    if(ShortestDistance > distance)
                    {
                        ShortestDistance = distance;
                        closestAttraction = tp;
                    }
                }
            }
            if (closestAttraction == null) { this.isFinishTrack = true; }
            else
            {
                this.currentAttractionDestination = closestAttraction;
                this.destinations[closestAttraction] = true;
            }
        }*/
        
        public async Task SignUp(string name, string socialNetwork)
        {
            this.currentUser = await conn.SignUp(name, socialNetwork);
        }
    }
}
