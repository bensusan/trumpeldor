
describe("Go to the Homepage ", function(){
   browser.ignoreSynchronization=true; // This allows to protractor to run on regular website, not specific to angular

  // it("Go to the Home page ", function(){
  //   browser.get("http://132.73.201.223:12345/main/"); // Go to a specific URL
  //   console.log("Home Page Open succesffully"); // Log a message
  // });
  //
  // it("Go to the attractions page ", function(){
  //   // var pendants = element(by.id("manage_attr_page")); // set a variable for action
  //   // pendants.click(); // Click on element
  //   let nekuda = browser.findElement(By.id("manage_attr_page"));
  //   nekuda.click();
  //   console.log("attr page succesffully"); // Log a message
  // });
  it("Go to the Home page ", function(){
    browser.get("https://www.google.com/"); // Go to a specific URL
    console.log("Home Page Open succesffully"); // Log a message
  });

  it("Go to the attractions page ", function(){
    // var pendants = element(by.id("manage_attr_page")); // set a variable for action
    // pendants.click(); // Click on element
    browser.get("https://www.google.com/");
    let nekuda = browser.findElement(By.name("q")).sendKeys("shmul");
    Keys.ENTER.click();
    //nekuda.click();
    console.log("attr page succesffully"); // Log a message
  });

    // From the Home Page go to the  Pendant Page
  // it("Go to Pendants Page ", function(){
  //   var pendants = element(by.css("#tm_menu > div > ul > li:nth-child(2) > a")); // set a variable for action
  //   pendants.click(); // Click on element
  //  // browser.sleep(1000) // Tell Protractor to Wait for 5000 miliseconds or 5 seconds
  //   console.log("From the Home Page go to the Pendant Page ");
  //   element(by.css("#content > div:nth-child(2) > div:nth-child(1) > div.product-thumb.transition.options > div.caption > div >  a")).click(); // Go the element and Click
  //   // browser.sleep(1000)
  //   console.log("Go to a specific Product Page");
  //  // browser.sleep(1000)
  //   browser.navigate().back(); // Tell the browser to go back
  // });

});