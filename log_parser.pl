use strict;
use warnings;
use Time::Piece;

sub parse_between_times {
    my ($s, $e, $file) = @_;
    # grabs total count of entries made between two given times for a given windows log file
    # inputs: 
    # s --> Start time: "01:34:00" "%H:%M:%S"
    # e --> End time: "01:39:59" "%H:%M:%S"
    # file --> filename: "application-event-log.txt"
    #
    # returns: 
    # count --> total count of entries between start and end time

    my $count = 0;
    
    # convert the times wanted based off military time. 
    my $start = Time::Piece->strptime($s, "%H:%M:%S");
    my $end = Time::Piece->strptime($e, "%H:%M:%S");
    
    # open file and get rid of headers
    open(my $file_handle, '<', $file) or die "Could not open '$file': $!";
    my $templ = <$file_handle>;

    # count number of entries between start and end times
    while (my $line = <$file_handle>) {
        my @columns = split /\t/, $line;
        my $time_object = Time::Piece->strptime($columns[2], "%I:%M:%S %p");
        if ($time_object >= $start && $time_object <= $end){
            $count++;
        }
    }

    return $count;
}

# Inputs
my $start_ = "01:34:00";
my $end_ = "01:39:59";
my $file_path_ = "application-event-log.txt";

my $count_entries = parse_between_times($start_, $end_, $file_path_);

# Output
print "Total count of log entries between $start_ and $end_ was --> $count_entries";
