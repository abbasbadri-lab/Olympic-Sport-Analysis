from flask import Flask, render_template

app = Flask(__name__)

# Updated Tableau Public Embed URLs with embed=y parameters
TABLEAU_LINKS = {
    "dash1": "https://public.tableau.com/views/Global_Olympic_Performance_Analysis-dashboard1/GLOBALOLYMPICPERFORMANCEANALYSIS?:embed=y&:showVizHome=n&:apiJSVersion=2",
    "dash2": "https://public.tableau.com/views/Global_Olympic_Performance_Analysis-dashboard1_17932100843500/ATHLETEREGIONALINSIGHTS?:embed=y&:showVizHome=n&:apiJSVersion=2",
    "dash3": "https://public.tableau.com/views/Global_Olympic_Performance_Analysis-dashboard1_17932100843500/HOSTINVESTMENTINSIGHTS?:embed=y&:showVizHome=n&:apiJSVersion=2",
    "story1": "https://public.tableau.com/views/Global_Olympic_Performance_Analysis-dashboard1_17932100843500/Story1GlobalOlympicGamesPerformanceTrends?:embed=y&:showVizHome=n&:apiJSVersion=2",
    "story2": "https://public.tableau.com/views/Global_Olympic_Performance_Analysis-dashboard1_17932100843500/Story2AthleteRegionalInsights?:embed=y&:showVizHome=n&:apiJSVersion=2",
    "story3": "https://public.tableau.com/views/Global_Olympic_Performance_Analysis-dashboard1_17932100843500/Story3HostAdvantageInvestmentPatterns?:embed=y&:showVizHome=n&:apiJSVersion=2",
    "story4": "https://public.tableau.com/views/Global_Olympic_Performance_Analysis-dashboard1_17932100843500/Story4KeyFindingsConclusion?:embed=y&:showVizHome=n&:apiJSVersion=2"
}

@app.route('/')
def home():
    return render_template('index.html', links=TABLEAU_LINKS)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', links=TABLEAU_LINKS)

@app.route('/story')
def story():
    return render_template('story.html', links=TABLEAU_LINKS)

if __name__ == '__main__':
    app.run(debug=True, port=5000)