import React, { Component, Fragment } from 'react';
import { withStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Grid from '@material-ui/core/Grid';
import Card from '@material-ui/core/Card';
import CardHeader from '@material-ui/core/CardHeader';
import CardContent from '@material-ui/core/CardContent';
import LinearProgress from "@material-ui/core/LinearProgress";
import Typography from '@material-ui/core/Typography';
import { skills } from '../../static/json/skills';

const styles = theme => ({
    root: {
        flexGrow: 1,
        backgroundColor: 'white',
    },
    text: {
        padding: theme.spacing(3, 0, 3),
        textTransform: "uppercase",
        textAlign: 'center',
    },
    cardRoot: {
        width: '100%',
        height: '100%',
    },
    cardHeader: {
        minHeight: 100
    }
});

const BorderLinearProgress = withStyles((theme) => ({
    root: {
      height: 5,
      borderRadius: 2,
    },
    colorPrimary: {
      backgroundColor: theme.palette.grey[theme.palette.type === 'light' ? 200 : 700],
    },
    bar: {
      borderRadius: 2,
      backgroundColor: '#1a90ff',
    },
  }))(LinearProgress);
  

class Skills extends Component {

    render() {
        const { classes } = this.props;

        return (
            <Fragment>
                <Container className={classes.root}>
                    <Typography className={classes.text} variant="h5">
                        Skills
                    </Typography>
                </Container>
                <Container className={classes.root}>
                    <Grid container>
                        {skills.map((skill, index) => {
                            return (
                                <Grid key={index} item xs sm md>
                                    <Card className={classes.cardRoot}>
                                        <CardHeader title={skill.name} className={classes.cardHeader} />
                                        <CardContent>
                                            <Grid container direction="column" spacing={1}>
                                                {skill.keywords.map((keyword, key) => {
                                                    return (
                                                        <Fragment key={key}>
                                                            <Grid item xs sm md>
                                                                <Typography variant="subtitle1">
                                                                    {keyword.name}
                                                                </Typography>
                                                            </Grid>
                                                            <Grid item xs sm md>
                                                                <BorderLinearProgress 
                                                                    variant="determinate"
                                                                    value={keyword.level}
                                                                />
                                                            </Grid>
                                                        </Fragment>
                                                    )
                                                })}
                                            </Grid>
                                        </CardContent>
                                    </Card>
                                </Grid>
                            )
                        })}
                    </Grid>
                </Container>
            </Fragment>
        );
    }
}

export default withStyles(styles)(Skills);