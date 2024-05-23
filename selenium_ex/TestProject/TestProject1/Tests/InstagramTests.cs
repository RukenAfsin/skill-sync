using NUnit.Framework;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using TestProject1.Pages.Concrete;
using x= TestProject1.UserInfo;

namespace TestProject1.Tests
{
    public class InstagramTests
    {
        private IWebDriver _driver;
        private UserService _userService;
        private x.UserInfo _userInfo;

        [SetUp]
        public void Setup()
        {
            string driverPath = @"C:\Users\User\Desktop\Applications\SkillSync\selenium_ex\TestProject\TestProject1\drivers\Chrome\chromedriver.exe";
            _driver = new ChromeDriver(driverPath);
            _userService = new UserService(_driver);
            _userInfo = new x.UserInfo();
        }

        [Test]
        public void LoginTest()
        {
            _userService.TrueLogin(_userInfo.Username, _userInfo.Password);
        }

        [Test]
        public void LogoutTest()
        {
            _userService.TrueLogin(_userInfo.Username, _userInfo.Password);
            _userService.Logout();
        }




        [TearDown]
        public void Teardown()
        {
            _driver.Quit();
        }
    }
}
