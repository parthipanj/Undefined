import React, { Component, Fragment } from 'react';
import { withStyles } from '@material-ui/core/styles';
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';
import Divider from '@material-ui/core/Divider';
import Card from '@material-ui/core/Card';
import CardContent from '@material-ui/core/CardContent';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import { experiences } from '../../static/json/experiences';

const styles = theme => ({
    root: {
        flexGrow: 1,
        backgroundColor: 'white',
    },
    text: {
        padding: theme.spacing(3, 0, 3),
        textTransform: 'uppercase',
        textAlign: 'center',
    },
    gridItem: {
        margin: 'auto',
        width: 850,
        height: '100%',
        maxWidth: '100%',
        maxHeight: '100%',
    },
    cardRoot: {
        display: 'flex',
        width: '100%',
    },
    details: {
        display: 'flex',
        flexDirection: 'column',
        textAlign: 'end',
        width: '50%',
    },
    cardContent: {
        flex: '1 0 auto',
        width: '50%',
    }
});

class Experience extends Component {

    render() {
        const { classes } = this.props;

        return (
            <Fragment>
                <Container className={classes.root}>
                    <Typography className={classes.text} variant='h5'>
                        Experience
                    </Typography>
                </Container>
                <Container className={classes.root}>
                    <List>
                        {experiences.map((experience, index) => {
                            return (
                                <ListItem key={index} className={classes.gridItem}>
                                    <Card className={classes.cardRoot} elevation={0}>
                                        <CardContent border={0} className={classes.details}>
                                            <Typography component='h5' variant='h5'>{`${experience.startDate} - ${experience.endDate}`}</Typography>
                                            <Typography variant='subtitle1' color='textSecondary'>{experience.position}</Typography>
                                        </CardContent>
                                        <Divider orientation='vertical' flexItem />
                                        <CardContent border={0} className={classes.cardContent}>
                                            <Typography component='h5' variant='h5'>{`${experience.company}, ${experience.location}`}</Typography>
                                            <Typography variant='subtitle1' color='textSecondary'>
                                                <List component="ul">
                                                    {experience.highlights.map((highlight, key) => {
                                                        return (
                                                            <ListItem key={key} dense disableGutters alignItems='flex-start'>
                                                                <ListItemText primary={`${highlight}`} />
                                                            </ListItem>
                                                        )
                                                    })}
                                                </List>
                                            </Typography>
                                        </CardContent>
                                    </Card>
                                </ListItem>
                            )
                        })}
                    </List>
                </Container>
            </Fragment >
        );
    }
}

export default withStyles(styles)(Experience);