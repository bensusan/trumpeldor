using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.IO;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using trumpeldor.SheredClasses;
using File = trumpeldor.SheredClasses.File;

namespace trumpeldor
{
    class ServerConection
    {
        public readonly static string IP = "132.72.23.64";
        //public readonly static string IP = "192.168.43.194";
        public readonly static string PORT = "12345";
        private readonly String urlPrefix = "http://" + IP +":" + PORT + "/usersystem/";
        public ServerConection()
        {
        }
        
        public Attraction GetAttractionById(string id)
        {
            //track point with all information
            //return new Attraction(1,"a", (float)31.262485, (float)34.803953);
            return null;
            //TODO
        }
        public List<Clue> GetAttractionClues(string id)
        {
            return new List<Clue>();
            //TODO
        }
        public Game GetAttractionGame(string id)
        {
            return new AQ();
            //TODO
        }
        public Game GetAttractionAmericanQuestion(string id)
        {
            return new AQ();
            //TODO
        }

        public async Task<User> SignUp(String name, String socialNetwork)
        {
            //User { name = name, socialNetwork = socialNetwork, lastSeen = null, email = null };
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

        internal async Task<Trip> CreateTripAsync(User currentUser, string groupName, List<int> playersAges, int trackLength, float xUser, float yUser)
        {
            var toSend = new { user = currentUser, groupName = groupName, playersAges = playersAges, trackLength = trackLength, x = xUser, y = yUser };
            string jsonResponse = await SendToServerAndGetResponseBack(toSend, "createTrip/");
            return JsonConvert.DeserializeObject<Trip>(jsonResponse);
        }

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
