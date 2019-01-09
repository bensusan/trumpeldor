using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using trumpeldor.SheredClasses;

namespace trumpeldor
{
    class ServerConection
    {
        //public readonly static string IP = "132.72.23.64";
        public readonly static string IP = "132.72.213.116";
        public readonly static string PORT = "12345";
        private readonly String urlPrefix = "http://" + IP +":" + PORT + "/usersystem/";
        public ServerConection()
        {
        }
        
        public async Task<User> SignUp(String name, String socialNetwork)
        {
            var newUser = new
            {
                name = name,
                socialNetwork = socialNetwork,
            };
            string jsonResponse = await SendToServerAndGetResponseBack(newUser, "signUp/");
            return JsonConvert.DeserializeObject<User>(jsonResponse);
        }

        internal async Task<KeyValuePair<string, List<int>>> LoadRelevantInformationFromLastTrip(User currentUser)
        {
            string jsonResponse = await SendToServerAndGetResponseBack(currentUser, "getRelevantPreviousTripInformation/");
            return JsonConvert.DeserializeObject<KeyValuePair<string, List<int>>>(jsonResponse);
        }

        internal async Task GetFullAttraction(Attraction attraction)
        {
            attraction.hints = await GetHintsByAttraction(attraction);
            attraction.americanQuestion = await GetAmericanQuestionByAttraction(attraction);
        }

        private class HelpHints
        {
            public List<Hint> hints { get; set; }
        }

        internal async Task<List<Hint>> GetHintsByAttraction(Attraction attraction)
        {
            string jsonResponse = await SendToServerAndGetResponseBack(new { id = attraction.id, }, "getHints/");
            jsonResponse = "{ 'hints': " + jsonResponse + "}";
            return JsonConvert.DeserializeObject<HelpHints>(jsonResponse).hints;
        }

        internal async Task<AmericanQuestion> GetAmericanQuestionByAttraction(Attraction attraction)
        {
            string jsonResponse = await SendToServerAndGetResponseBack(new { id = attraction.id, }, "getAmericanQuestion/");
            return JsonConvert.DeserializeObject<AmericanQuestion>(jsonResponse);
        }

        class HelpFeedbacks
        {
            public List<FeedbackInstance> feedbacks { get; set; }
        }

        private async Task<List<FeedbackInstance>> GetFeedbacks(Trip trip)
        {
            string jsonResponse = await SendToServerAndGetResponseBack(new { id = trip.id, }, "getFeedbacks/");
            jsonResponse = "{ 'feedbacks': " + jsonResponse + "}";
            HelpFeedbacks hf = JsonConvert.DeserializeObject<HelpFeedbacks>(jsonResponse);
            return hf.feedbacks;
        }

        //private class TripDB
        //{
        //        public int user { get; set; }
        //        public string groupName { get; set; }
        //        public List<int> playersAges { get; set; }
        //        public int score { get; set; }
        //        public int track { get; set; }
        //        public List<int> attractionsDone { get; set; }
        //}


        internal async Task<Trip> CreateTripAsync(User currentUser, string groupName, List<int> playersAges, int trackLength, float xUser, float yUser)
        {
            var toSend = new { user = currentUser, groupName = groupName, playersAges = playersAges, trackLength = trackLength, x = xUser, y = yUser, };
            string jsonResponse = await SendToServerAndGetResponseBack(toSend, "createTrip/");
            Trip trip = JsonConvert.DeserializeObject<Trip>(jsonResponse);
            //string jsonResponse = await SendToServerAndGetResponseBack(toSend, "createTrip/");
            //Trip trip = JsonConvert.DeserializeObject<Trip>(jsonResponse);
            //trip.groupName = tripDB.groupName; trip.playersAges = tripDB.playersAges; trip.score = tripDB.score;
            //trip.user = await GetUserById(tripDB.user);
            trip.attractionsDone = await GetFullAttractions(trip.attractionsDone);
            trip.track = await GetFullTrack(trip.track);
            trip.feedbacks = await GetFeedbacks(trip);            
            return trip;
        }

        internal async Task<Track> GetFullTrack(Track track)
        {
            if (track.subTrack != null)
                track.subTrack = await GetFullTrack(track.subTrack);
            track.points = await GetFullAttractions(track.points);
            return track;
        }

        internal async Task<List<Attraction>> GetFullAttractions(List<Attraction> attractions)
        {
            foreach (Attraction attraction in attractions)
                await GetFullAttraction(attraction);
            return attractions;
        }

        //internal async Task<User> GetUserById(int user)
        //{
        //    string jsonResponse = await SendToServerAndGetResponseBack(new { user = user }, "getUserById/");
        //    return JsonConvert.DeserializeObject<User>(jsonResponse);
        //}

        internal async Task<Trip> GetPreviousTrip(User currentUser)
        {
            string jsonResponse = await SendToServerAndGetResponseBack(currentUser, "previousTrip/");
            return JsonConvert.DeserializeObject<Trip>(jsonResponse);
        }

        public StringContent ContentPost(Object obj)
        {
            var json = JsonConvert.SerializeObject(obj);
            var content = new StringContent(json, Encoding.UTF8, "application/json");
            return content;
        }

        private async Task<string> SendToServerAndGetResponseBack(Object toSend, string endOfUri)
        {
            using (var client = new HttpClient())
            {
                var content = ContentPost(toSend);

                //  send a POST request  
                var uri = urlPrefix + endOfUri;
                var response = await client.PostAsync(uri, content);

                // on error throw a exception  
                response.EnsureSuccessStatusCode();
                return await response.Content.ReadAsStringAsync();
            }
        }

        private async Task<string> GetFromServer(HttpClient client, string endOfUri)
        {
            var uri = urlPrefix + endOfUri;
            return await client.GetStringAsync(uri);
        }
    }
}
