using OpenQA.Selenium;
using OpenQA.Selenium.Support.UI;
using SeleniumExtras.WaitHelpers;
using System.IO;
using TestProject1.Business.Abstract;
using TestProject1.Pages;

namespace TestProject1.Business.Concrete
{
    public class ProfileService : IProfileService
    {
        public readonly IWebDriver _driver;
        public readonly ProfilePage _profilePage;

        public ProfileService(IWebDriver driver)
        {
            _driver = driver;
            _profilePage = new ProfilePage(_driver);
        }

        public void GetFollowers()
        {
            WebDriverWait wait = new WebDriverWait(_driver, TimeSpan.FromSeconds(10));
            wait.Until(ExpectedConditions.ElementIsVisible(By.CssSelector("ul.x78zum5 li:nth-child(2)")));
            if (_profilePage.SecondLiElement.Displayed)
            {
                _profilePage.SecondLiElement.Click();
                Thread.Sleep(7000);

                string followersCount = _profilePage.SecondLiElement.Text;
                string csvFilePath = @"C:\Users\User\Desktop\Applications\SkillSync\selenium_ex\TestProject\TestProject1\followers.csv";
                WriteDataToCSV(csvFilePath, followersCount);
            }
        }

        public void GetFollowing()
        {
            WebDriverWait wait = new WebDriverWait(_driver, TimeSpan.FromSeconds(10));
            wait.Until(ExpectedConditions.ElementIsVisible(By.CssSelector("ul.x78zum5 li:nth-child(3)")));
            if (_profilePage.ThirdLiElement.Displayed)
            {
                _profilePage.ThirdLiElement.Click();
                Thread.Sleep(7000);

                string followingCount = _profilePage.ThirdLiElement.Text;
                string csvFilePath = @"C:\Users\User\Desktop\Applications\SkillSync\selenium_ex\TestProject\TestProject1\following.csv"; 
                WriteDataToCSV(csvFilePath, followingCount);
            }
        }


        private void WriteDataToCSV(string filePath, string data)
        {
            using (StreamWriter writer = new StreamWriter(filePath))
            {
                writer.WriteLine("Count");
                writer.WriteLine(data);
            }
        }

        public void GetYourFollowers(string follower)
        {
            WebDriverWait wait = new WebDriverWait(_driver, TimeSpan.FromSeconds(10));
            wait.Until(ExpectedConditions.ElementIsVisible(By.CssSelector("input[aria-label='Arama Girdisi']")));
            if (_profilePage.SecondLiElement.Displayed)
            {
                _profilePage.SecondLiElement.Click();
                Thread.Sleep(7000);
                _profilePage.GetFollowerSearchButton.SendKeys(follower);

            }
        }
    }
}
