using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Text;
using System.Threading.Tasks;
using trumpeldor.SheredClasses;

namespace trumpeldor
{
    class ServerConection
    {
        private readonly String urlPrefix = "http://192.168.43.194:12345/usersystem/";
        public ServerConection()
        {

        }

        
        public TrackPoint GetTrackPointById(string id)
        {
            //track point with all information
            return new TrackPoint(31.262485, 34.803953);
            //TODO
        }
        public List<Clue> GetTrackPointClues(string id)
        {
            return new List<Clue>();
            //TODO
        }
        public Game GetTrackPointGame(string id)
        {
            return new AQ();
            //TODO
        }
        public Game GetTrackPointAmericanQuestion(string id)
        {
            return new AQ();
            //TODO
        }

        public String GetGeneralInformation()
        {

            //TODO
            return "some general information";
        }



        /////
        ///

        public async Task getFeedbackAsync()
        {
            Task<String> result = resultGetAsync(urlPrefix + "feedback/");
            var posts = JsonConvert.DeserializeObject<List<FeedBack>>(await result);
        }

        public async Task<User> SignUp(String name, String socialNetwork)
        {
            using (var client = new HttpClient())
            {
                // Create a new post  
                var newUser = new User
                {
                    name = name,
                    socialNetwork = socialNetwork,
                    //playersAges = playersAges,
                    //lastSeen = lastSeen,
                    //email = userEmail
                };


                //var content = contentPost(newUser);

                ////  send a POST request  
                //var uri = urlPrefix + "signUp/";
                //var response = await client.PostAsync(uri, content);

                //// on error throw a exception  
                //response.EnsureSuccessStatusCode();
                //string responseBody = await response.Content.ReadAsStringAsync();

                string jsonResponse = await SendToServer(client, newUser, "signUp/");
                return JsonConvert.DeserializeObject<User>(jsonResponse);
                // handling an answer maybe in the future  

            }
        }

        public async Task<byte[]> getFile()
        {
            //HttpClient client = new HttpClient();
            //var byteArray = Encoding.ASCII.GetBytes("username:password");
            //client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Basic", Convert.ToBase64String(byteArray));
            using (var client = new HttpClient())
            {
                var uri = urlPrefix + "getFile/";
                HttpResponseMessage response = await client.GetAsync(uri);
                byte[] myBytes = await response.Content.ReadAsByteArrayAsync();


                return myBytes;
            }

            // string convertedFromString = Convert.ToBase64String(myBytes);

            // return "data:image/png;base64," + convertedFromString;
        }


        public async Task<String> resultGetAsync(String uri)
        {
            using (var client = new HttpClient())
            {
                return await client.GetStringAsync(uri);
            }
        }

        public StringContent contentPost(Object obj)
        {
            var json = JsonConvert.SerializeObject(obj);
            var content = new StringContent(json, Encoding.UTF8, "application/json");
            return content;
        }

        private async Task<string> SendToServer(HttpClient client, Object toSend, string endOfUri)
        {
            var content = contentPost(toSend);

            //  send a POST request  
            var uri = urlPrefix + endOfUri;
            var response = await client.PostAsync(uri, content);

            // on error throw a exception  
            response.EnsureSuccessStatusCode();
            return await response.Content.ReadAsStringAsync();
        }
    }
}
