import React, { Component, Fragment } from 'react';
import { withStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Grid from '@material-ui/core/Grid';
import Box from '@material-ui/core/Box';
import Link from '@material-ui/core/Link';
import Typography from '@material-ui/core/Typography';
import CardMedia from '@material-ui/core/CardMedia';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import { ListItemIcon } from '@material-ui/core';
import LinkedInIcon from '@material-ui/icons/LinkedIn';
import TwitterIcon from '@material-ui/icons/Twitter';
import background from '../../static/images/background.png';
import profile from '../../static/images/profile.jpg';

const styles = () => ({
    root: {
        backgroundImage: `url(${background})`,
        flexGrow: 1,
        paddingTop: 40,
    },
    gridContainer: {
        margin: 'auto',
        width: 650,
        height: '100%',
        maxWidth: '100%',
        maxHeight: '100%',
        backgroundColor: 'rgba(241, 241, 241, 1)',
    },
    img: {
        maxHeight: '100%',
        minHeight: 400
    },
    profileList: {
        margin: '0 0 0 50px',
    },
    social: {
        minHeight: 50,
        backgroundColor: 'rgba(24, 33, 83, 1)'
    },
    socialList: {
        textAlign: 'center'
    },
    summaryContainer: {
        flexGrow: 1,
        backgroundColor: 'rgba(241, 241, 241, 1)',
        textAlign: 'center',
        padding: 50,
        minHeight: 250
    },
    summaryBoxDiv: {
        position: 'relative'
    },
    summarySpan: {
        font: 'normal normal normal 30px/1.4em avenir-lt-w01_35-light1475496,sans-serif',
        color: '#182153'
    },
    summaryParagraph: {
        font: 'normal normal normal 18px/1.4em avenir-lt-w01_35-light1475496,sans-serif',
        color: '#182153'
    }
});

class Profile extends Component {

    render() {
        const { classes } = this.props;

        return (
            <Fragment>
                <Container className={classes.root}>
                    <Grid container direction='column' className={classes.gridContainer}>
                        <Grid item container direction='row'>
                            <Grid item xs sm md>
                                <CardMedia
                                    component="img"
                                    className={classes.img}
                                    image={profile}
                                    title='Parthipan J'
                                    alt='Parthipan J'
                                />
                            </Grid>
                            <Grid item xs sm md>
                                <List className={classes.profileList}>
                                    <ListItem>
                                        <ListItemText disableTypography
                                            primary={<Typography variant="h4" color="primary"> Parthipan J </Typography>}
                                            secondary={<Typography variant="subtitle2" color="textSecondary"> Senior Application Developer </Typography>}
                                        />
                                    </ListItem>
                                    <ListItem>
                                        <ListItemText primary="Phone:" secondary="8675540893" />
                                    </ListItem>
                                    <ListItem>
                                        <ListItemText primary="Email:" secondary="parthij15@gmail.com" />
                                    </ListItem>
                                    <ListItem>
                                        <ListItemText primary="Date of Birth:" secondary="May 20th, 1993" />
                                    </ListItem>
                                    <ListItem>
                                        <ListItemText primary="Location:" secondary="Chennai, TN, India" />
                                    </ListItem>
                                </List>
                            </Grid>
                        </Grid>
                        <Grid item xs sm md className={classes.social}>
                            <List className={classes.socialList}>
                                <ListItemIcon >
                                    <Link href={`https://linkedin.com/in/parthipanj`} target="_blank" rel="noreferrer"> <LinkedInIcon style={{ color: 'white' }} /> </Link>
                                </ListItemIcon >
                                <ListItemIcon >
                                    <Link href={`https://twitter.com/Parthipan_J`} target="_blank" rel="noreferrer"> <TwitterIcon style={{ color: 'white' }} /> </Link>
                                </ListItemIcon >
                            </List>
                        </Grid>
                    </Grid>
                </Container>
                <Container fixed className={classes.summaryContainer}>
                    <Box component='div' className={classes.summaryBoxDiv} >
                        <Box component="span" className={classes.summarySpan}>
                            Hello! I'm Parthi
                        </Box>
                        <Box component='p' className={classes.summaryParagraph}>
                            Software Engineer with 3.5+ years of experience. Interested to learn new languages, technologies, and tools.

                            Here is my tech stack: Python, Javascript, Java (Beginner), Scala (Beginner), MongoDB, Apache Cassandra, MySQL, HBase (Beginner), Elasticsearch, Apache Kafka, Apache Spark (Beginner), RabbitMQ, and Docker.

                            Having experience in various frameworks and libraries like Django Rest, React, Springboot.

                            Also having knowledge in the DevOps, TDD, Agile, Microservices.

                            Gucci!!!
                        </Box>
                    </Box>
                </Container>
            </Fragment>
        );
    }
}

export default withStyles(styles)(Profile);